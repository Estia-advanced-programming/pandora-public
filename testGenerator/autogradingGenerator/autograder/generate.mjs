/* eslint max-params : "off" */
import { Metadata, Records } from "./lib/models.mjs" ;
import fs from "fs" ;
import { join } from "path" ;
import jsonPrint from "json-beautify" ;
import { toDo } from "./ressources/testDescription.mjs" ;

let gid = 0 ;
const tests =
{ milestones : {}
, tests      : [] } ;
generate() ;
export default function generate() {
  for ( const index in toDo.milestones ) {
    const milestone = toDo.milestones[ index ] ;
    for( const feature in milestone ) {
      const testDescriptions = Array.prototype.concat( milestone[ feature ] ) ;
      for( const testDescription of testDescriptions ) createSuite( index, testDescription ) ;
    }
  }

  fs.writeFile( "testsFiles/testSuite.json", jsonPrint( tests.tests, null, 2, 80 ), "utf8", err => err && console.log( err ) ) ;
  console.table( tests.tests ) ;
}

function createSuite( milestone, { suffix, types, values, result, input } ) {
  if( types ) {
    for( const type of types ) {
      createMinMaxSuite( milestone, type, suffix, input, ( type === "min" ) ? 1000 : 0 ) ;
    }
  } else {
    const id = registerTest( milestone, suffix, result ) ;
    createTestFile( milestone, suffix, id, {}, createInput( input, values ), 0 ) ;
  }
}


function createMinMaxSuite( milestone, type, _name, input, restValue = 0, metadata = {} ) {
  const name = type + _name ;
  // integer value
  if( input instanceof Array ) metadata.motors = input.filter( e => e.match( /engine_\d/ ) ).length ;
  let r = 100 ;
  let values = createInput( input, [ r, r, r, r ] ) ;
  let resultat = computeResultat( type, input, values ) ;
  let id = registerTest( milestone, name, resultat ) ;
  createTestFile( milestone, name, id, metadata, values, restValue ) ;
  // integer negative value
  r = -100 ;
  values = createInput( input, [ r, r, r, r ] ) ;
  resultat = computeResultat( type, input, values ) ;
  id = registerTest( milestone, name, resultat ) ;
  createTestFile( milestone, name, id, metadata, values, restValue ) ;
  // one line
  r = 100 ;
  values = createInput( input, [ r ] ) ;
  resultat = computeResultat( type, input, values ) ;
  id = registerTest( milestone, name, resultat ) ;
  createTestFile( milestone, name, id, metadata, values, restValue ) ;
  // float values
  r = round( Math.random() * 1000 ) ;
  values = createInput( input, [ r, r, r, r ] ) ;
  resultat = computeResultat( type, input, values ) ;
  id = registerTest( milestone, name, resultat ) ;
  createTestFile( milestone, name, id, metadata, values, restValue ) ;
  // different position values
  r = round( Math.random() * 1000 ) ;
  values = createInput( input, [ r, restValue, restValue, restValue ] ) ;
  resultat = computeResultat( type, input, values ) ;
  id = registerTest( milestone, name, resultat ) ;
  createTestFile( milestone, name, id, metadata, values, restValue ) ;
  values = createInput( input, [ restValue, r, restValue, restValue ] ) ;
  id = registerTest( milestone, name, resultat ) ;
  createTestFile( milestone, name, id, metadata, values, restValue ) ;
  values = createInput( input, [ restValue, restValue, restValue, r ] ) ;
  id = registerTest( milestone, name, resultat ) ;
  createTestFile( milestone, name, id, metadata, values, restValue ) ;

}


function registerTest( milestone, feature, result ) {
  const test =
  { id        : gid++
  , milestone : milestone
  , feature   : feature
  , file      : ""
  , result    : result } ;

  if( !Object.hasOwnProperty.call( tests.milestones, milestone ) ) {
    tests.milestones[ milestone ] = { features: {} } ;
  }
  if( !Object.hasOwnProperty.call( tests.milestones[ milestone ].features, feature ) ) {
    tests.milestones[ milestone ].features[ feature ] = [] ;
  }
  tests.tests.push( test ) ;
  const id = tests
    .milestones[ milestone ]
    .features[ feature ]
    .push( test ) ;
  test.file = filePath( milestone, feature, id ) ;
  return id ;
}


function createTestFile( milestone, name, id, _metadata, values, restValue = 0 ) {
  const { origin, motors, airports, mass } = _metadata ;
  const metadata = new Metadata( id, origin, motors, airports, mass ) ;
  const records = new Records( values, motors, restValue ) ;
  const path = directoryPath( milestone ) ;
  fs.exists( path, exist => {
    if( exist ) writeFlightRecord( filePath( milestone, name, id ), metadata, records ) ;
    else fs.mkdir( path, err => !err && writeFlightRecord( filePath( milestone, name, id ), metadata, records ) ) ;
  } ) ;
}


/**
 * writeFlightRecord - Write the file
 *
 * @param  {Path} filename where to save the flightrecord
 * @param  {Object} metadata what to put in the metadata section
 * @param  {Records[]} records  description
*/
function writeFlightRecord( filename, metadata, records ) {
  let data = metadata.toString() ;
  data += "\n" ;
  data += records.toString() ;
  fs.writeFile( filename, data, handleError ) ;
}


/**
 * handleError - just print the error
 *
 * @param  {Error} err the error to print
  */
function handleError( err ) {
  if( err ) console.error( err ) ;
}

function directoryPath( milestone ) {
  return join( "./testsFiles/", milestone ) ;
}

function filePath( milestone, feature, id ) {
  return join( directoryPath( milestone ), feature + "_" + id + ".frd" ) ;
}

function createInput( input, values ) {
  const object = {} ;
  const inputs = Array.prototype.concat( input ) ;
  object.timestamp = [] ;

  if( values instanceof Array ) {
    for( const i in values ) object.timestamp.push( i ) ;
    for( const input of inputs ) object[ input ] = values ;
  } else if( typeof values === "object" ) {
    let length = 0 ;
    for( const input of inputs ) {
      object[ input ] = values[ input ] ;
      length = values[ input ].length ;
    }
    for( let i = 0 ; i < length ; i++ ) object.timestamp.push( i ) ;
  }

  return object ;
}

function computeResultat( type, input, values ) {
  let finalResult = 0 ;
  const inputs = Array.prototype.concat( input ) ;
  for( const input of inputs ) {
    switch( type ) {
    case "max": finalResult += values[ input ].reduce( ( acc, e ) => Math.max( acc, e ) ) ; break ;
    case "min": finalResult += values[ input ].reduce( ( acc, e ) => Math.min( acc, e ) ) ; break ;
    case "avg": finalResult += values[ input ].reduce( ( acc, e ) => acc + e ) / values[ input ].length ; break ;
    default: return 0 ;
    }
  }
  return finalResult ;
}

function round( value, decimalPlace = 2 ) {
  const hundredth = Math.pow( 10, decimalPlace ) ;
  return Math.floor( value * hundredth ) / hundredth ;
}
