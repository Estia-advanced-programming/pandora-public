// From
export default function batchPromises( items, fn, options ) {
  const results = [] ;
  let index = ( options.batchSize - 1 ) ;

  function getNextItem() {
    index++ ;
    if ( items.length > index ) {
      const nextItem = items[ index ] ;
      return getCurrentItem( nextItem ) ;
    }
  }

  function getCurrentItem( item ) {
    return fn( item )
      .then( function( result ) {
        process.stdout.write( Math.round( 100 * index / items.length ) + "% " ) ;
        for( let i = 0 ; i < index % 3 ; i++ ) process.stdout.write( "." ) ;
        process.stdout.write( "     \r" ) ;
        results.push( result ) ;
        return getNextItem() ;
      } )
      .catch( function() {
        return options.retry ? getCurrentItem( item ) : getNextItem() ;
      } ) ;
  }
  const promises = items.slice( 0, options.batchSize ).map( function( item ) {
    return getCurrentItem( item ) ;
  } ) ;
  return Promise.all( promises ).then( function() {
    process.stdout.write( "\n" ) ;
    return results ;
  } ) ;
}
