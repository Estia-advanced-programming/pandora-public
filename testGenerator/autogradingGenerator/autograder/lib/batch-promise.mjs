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
        console.log( "." ) ;
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
    return results ;
  } ) ;
}
