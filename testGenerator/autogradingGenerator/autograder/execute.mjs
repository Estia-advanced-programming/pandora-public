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
{ batchSize : 20
, retry     : false
} ;


async function processTest( err, jsonFile ) {
  if( err ) { return console.error( err ) ; }
  const testSuite = JSON.parse( jsonFile ) ;
  try {
    await batchPromises( testSuite, handler, options ) ;
    console.table( testSuite ) ;
  } catch( e ) { console.log( e ) ; }
  return 0 ;
}

function reference( options, files ) {
  return constructCommand( "../../../release/pandora.jar", options, files ) ;
}
function pandora( options, files ) {
  return constructCommand( "/Users/dimitri/Documents/workspace/enseignement/2020/advancedProg/Archives/pandora-student/blackvisionmirror/target/pandora.jar", options, files ) ;
}

function constructCommand( jar, _option, _files ) {
  const options = Array.prototype.concat( _option ) ;
  const files = Array.prototype.concat( _files ) ;
  return "java -jar " + jar + " " + options.join( " " ) + " " + files.join( " " ) ;
}

function cleanOutput( string ) {
  // single line
  if( string.match( /\d+ (?<out>\d+\.?\d*)\n*/ ) ) return +string.match( /\d+ (?<out>\d+\.?\d*)\n*/ ).groups.out ;
  if( string.match( /(?<out>\d+\.?\d*)\n*/ ) ) return +string.match( /(?<out>\d+\.?\d*)\n*/ ).groups.out ;
  return string ;
}
