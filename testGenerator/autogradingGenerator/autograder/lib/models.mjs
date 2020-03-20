/* eslint max-classes-per-file: "off"*/
export class Metadata {
  constructor( testId, origin, motors, airports, mass ) {
    airports = airports || { source      : "vaziani"
    , destination : "gelendzhik" } ;
    mass = mass || { aircraft : 100
    , fuel     : 120 } ;
    this[ "flight id" ] = testId ;
    this[ "flight code" ] = "test" ;
    this.origin = origin || "RU" ;
    this.date = "2020-03-17" ;
    this.from = airports.source ;
    this.to = airports.destination ;
    this[ "motor(s)" ] = motors || 1 ;
    this[ "mass aircraft" ] = mass.aircraft ;
    this[ "mass fuel" ] = mass.fuel ;
    this[ "lift coef" ] = "1.60" ;
    this[ "drag coef" ] = "0.01" ;
  }

  toString() {
    let result = "" ;
    for( const key of Object.getOwnPropertyNames( this ) ) {
      result += `${ key }: ${ this[ key ] }\n` ;
    }
    return result ;
  }
}

export class Records {

  /**
   * constructor - description
   *
   * @param  {type} motors       description
   * @param  {Object} values       description
   * @param  {number[]} values.key
   * @param  {number} [defaultValue=0] default value if the key is not present
   * @return {type}              description
   */
  constructor( values, motors = 1, defaultValue = 0 ) {
    const header = [ "timestamp", "longitude", "latitude", "altitude", "roll", "pitch", "yaw", "heading", "air_speed", "temperature_in", "humidity_in", "pressure_in", "heart_rate", "oxygen_mask" ] ;
    const indiceEngine0 = header.indexOf( "temperature_in" ) ;
    for( let i = 0 ; i < motors ; i++ ) header.splice( indiceEngine0 + i, 0, `engine_${ i }` ) ;

    this.header = header ;
    this.values = [] ;

    // Determine the number of line in the record section
    let maxLine = 0 ;
    for( const key of header ) {
      // Create array if not exist
      if( !( values[ key ] instanceof Array ) ) values[ key ] = [ defaultValue ] ;
      maxLine = Math.max( maxLine, values[ key ].length ) ;
    }
    for( let i = 0 ; i < maxLine ; i++ ) {
      const line = [] ;
      for( const key of header ) {
        line.push( values[ key ][ i ] || defaultValue ) ;
      }
      this.values.push( line ) ;
    }
  }

  toString() {
    let result = "" ;
    for( const key of this.header ) {
      result += key + "," ;
    }
    // remove pending comma
    result = result.slice( 0, -1 ) ;
    for( const recordLine of this.values ) {
      let line = "\n" ;
      for( const value of recordLine ) {
        line += value + "," ;
      }
      line = line.slice( 0, -1 ) ;
      result += line ;
    }
    return result ;
  }
}
