import batchPromises from "./lib/batch-promise.mjs" ;
import fs from "fs" ;
import run from "./lib/runner.mjs" ;

fs.readFile( "./testsFiles/testSuite.json", "utf8", processTest ) ;

function handler( test ) {
  return new Promise( ( resolve, reject ) => {
    run( reference( [ "-o", test.feature ], test.file ), process.cwd() )
      .then( value => {
        test.reference = cleanOutput( value ) ;
        return run( pandora( [ "-o", test.feature ], test.file ), process.cwd() ) ;
      } )
      .then( value => {
        test.student = cleanOutput( value ) ;
        resolve( test ) ;
      } )
      . catch( reject ) ;
  } ) ;
}
const options =
{ batchSize : 10
, retry     : false
} ;


function score0( s ) {
  const factor = 10 ;
  return Math.floor( Math.pow( factor * factor, 1 - Math.abs( s ) ) / factor ) / factor ;
}

async function processTest( err, jsonFile ) {
  if( err ) { return console.error( err ) ; }
  const testSuite = JSON.parse( jsonFile ) ;
  try {
    await batchPromises( testSuite, handler, options ) ;
    for( const test of testSuite ) {
      delete test.id ;
      if( typeof test.result === "number" ) {
        if( test.result === 0 ) test.total = score0( test.student ) ;
        test.total = score0( ( test.student - test.result ) / test.result ) ;
      } else if( typeof test.reference === "number" ) {
        if( test.result === 0 ) test.total = score0( test.student ) ;
        test.total = score0( ( test.student - test.reference ) / test.reference ) ;
      } else {
        test.total = test.reference.match( test.student ) ? 1 : 0 ;
      }
    }
    console.table( testSuite ) ;
  } catch( e ) { console.log( e ) ; }
  return 0 ;
}

function reference( options, files ) {
  return constructCommand( "../../../release/pandora.jar", options, files ) ;
}
function pandora( options, files ) {
  return constructCommand( "/Users/dimitri/Documents/workspace/enseignement/2020/advancedProg/Archives/pandora-student/drt/target/pandora.jar", options, files ) ;
}

function constructCommand( jar, _option, _files ) {
  const options = Array.prototype.concat( _option ) ;
  const files = Array.prototype.concat( _files ) ;
  return "java -jar " + jar + " " + options.join( " " ) + " " + files.join( " " ) ;
}

function cleanOutput( string ) {
  // single line
  let regex = /(?<out>\d\d:\d\d:\d\d)\n*/ ;
  if( string.match( regex ) ) return string.match( regex ).groups.out ;
  regex = /^\d+ (?<out>-?\d+\.?\d*)\n*/ ;
  if( string.match( regex ) ) return +string.match( regex ).groups.out ;
  regex = /(?<out>-?\d+\.?\d*)\n*/ ;
  if( string.match( regex ) ) return +string.match( regex ).groups.out ;
  return string ;
}
