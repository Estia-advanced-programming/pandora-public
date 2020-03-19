import kill from "tree-kill" ;
import { spawn } from "child_process" ;

function waitForExit( child, timeout ) {
  // eslint-disable-next-line no-undef
  return new Promise( ( resolve, reject ) => {
    let timedOut = false ;
    const exitTimeout = setTimeout( () => {
      timedOut = true ;
      reject( new Error( `Timed out in ${ timeout } milliseconds` ) ) ;
      kill( child.pid ) ;
    }, timeout ) ;
    child.once( "exit", ( code, signal ) => {
      if ( timedOut ) return ;
      clearTimeout( exitTimeout ) ;
      if ( code === 0 ) {
        resolve( undefined ) ;
      } else {
        reject( new Error( `Error: Exit with code: ${ code } and signal: ${ signal }` ) ) ;
      }
    } ) ;
    child.once( "error", error => {
      if ( timedOut ) return ;
      clearTimeout( exitTimeout ) ;
      reject( error ) ;
    } ) ;
  } ) ;
}

export default function run( command, expectedValue, cwd ) {
  // const writeStream = fs.createWriteStream( "./output" ) ;
  return new Promise( resolve => {
    const child = spawn( command,
      { cwd
      , shell : true
      , env   :
        { PATH        : process.env.PATH
        , FORCE_COLOR : "true"
        }
      } ) ;

    let output = "" ;
    child.stdout.on( "data", chunk => true && ( output += chunk ) ) ;
    waitForExit( child, 300000 )
      .then( () => resolve( output ) )
      .catch( () => resolve( "ERROR" ) ) ;
  }
  ) ;
}
