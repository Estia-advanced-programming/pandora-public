export const toDo = { milestones:
  {
  milestone1:
    { altitude:
      { suffix : "Alt"
      , input  : "altitude"
      , types  : [ "avg", "max" ] }
    , airSpeed:
      { suffix : "AirSpeed"
      , input  : "air_speed"
      , types  : [ "avg", "max" ] }
    , enginePower:
    [ { suffix : "EnginePower"
    , input  : [ "engine_0" ]
    , types  : [ "avg", "max" ]
    }
    , { suffix : "EnginePower"
    , input  : [ "engine_0", "engine_1" ]
    , types  : [ "avg", "max" ]
    }
    , { suffix : "EnginePower"
    , input  : [ "engine_0", "engine_1", "engine_2", "engine_3" ]
    , types  : [ "avg", "max" ] }
    ]
    }
  , milestone2:
    { temperature:
      { suffix : "Temp"
      , input  : "temperature_in"
      , types  : [ "avg", "min", "max" ] }
    , pressure:
      { suffix : "Pressure"
      , input  : "pressure_in"
      , types  : [ "avg", "min", "max" ] }
    , humidity:
      { suffix : "Humidity"
      , input  : "humidity_in"
      , types  : [ "avg", "min", "max" ] }
    , heartRate:
      { suffix : "HeartRate"
      , input  : "heart_rate"
      , types  : [ "avg", "min", "max" ] }
    , oxygen:
      { suffix : "Oxygen"
      , input  : "oxygen_mask"
      , types  : [ "avg", "min", "max" ] }
    }
  , milestone3:
    { flightDuration:
        [
          { suffix : "flightDuration"
          , input  : "timestamp"
          , values : [ 0, 1 ]
          , result : "00:00:01"
          }
          , { suffix : "flightDuration"
          , input  : "timestamp"
          , values : [ 0, 60 ]
          , result : "00:01:00"
          }
          , { suffix : "flightDuration"
          , input  : "timestamp"
          , values : [ 0, 60.01 ]
          , result : "00:01:00"
          }
          , { suffix : "flightDuration"
          , input  : "timestamp"
          , values : [ 0, 3600 ]
          , result : "01:00:00"
          }
          , { suffix : "flightDuration"
          , input  : "timestamp"
          , values : [ 0, 25 * 3600 ]
          , result : "25:00:00"
          }
        ]
    , flightDistance:
        [ { suffix : "flightDistance"
        , input  : "altitude"
        , values : [ 0, 1000 ]
        , result : 1
        }
        , { suffix : "flightDistance"
        , input  : "latitude"
        , values : [ 0, 1 ]
        , result : 6371 / 360 * Math.PI * 2
        }
        , { suffix : "flightDistance"
        , input  : "longitude"
        , values : [ 0, 1 ]
        , result : 6371 / 360 * Math.PI * 2
        }
        , { suffix : "flightDistance"
        , input  : [ "longitude", "latitude" ]
        , values :
          { longitude : [ 0, 1 ]
          , latitude  : [ 0, 1 ] }
        , result: 6400 / 360 * Math.PI * 2 * Math.SQRT2
        }
        , { suffix : "flightDistance"
        , input  : [ "longitude", "altitude" ]
        , values :
          { longitude : [ 0, 1 ]
          , altitude  : [ 29000, 29000 ] }
        , result: 6400 / 360 * Math.PI * 2
        }
        ]
    , avgAcceleration:
        [ { suffix : "avgAcceleration"
        , input  : "longitude"
        , values : [ 0, 0.00000895 * 1, 0.00000895 * 2, 0.00000895 * 3, 0.00000895 * 4 ]
        , result : 0
        }
        , { suffix : "avgAcceleration"
        , input  : "longitude"
        , values : [ 0, 3 * 0.00000895 * 1, 3 * 0.00000895 * 3 ]
        , result : 1
        }
        , { suffix : "avgAcceleration"
        , input  : "longitude"
        , values : [ 0, 3 * 0.00000895 * 2, 3 * 0.00000895 * 3 ]
        , result : -1
        }
        , { suffix : "avgAcceleration"
        , input  : "longitude"
        , values : [ 0, 3 * 0.00000895 * 2, 3 * 0.00000895 * 3 ]
        , result : -1
        }
        , { suffix : "avgAcceleration"
        , input  : "altitude"
        , values : [ 0, 3 * 1, 3 * 3 ]
        , result : 1
        }
        ]
    , maxAcceleration:
        [ { suffix : "maxAcceleration"
        , input  : "longitude"
        , values : [ 0, 0.00000895 * 1, 0.00000895 * 2, 0.00000895 * 3, 0.00000895 * 4 ]
        , result : 0
        }
        , { suffix : "maxAcceleration"
        , input  : "longitude"
        , values : [ 0, 0.00000895 * 1, 0.00000895 * 3 ]
        , result : 1
        }
        , { suffix : "maxAcceleration"
        , input  : "longitude"
        , values : [ 0, 0.00000895 * 2, 0.00000895 * 3 ]
        , result : -1
        }
        , { suffix : "maxAcceleration"
        , input  : "longitude"
        , values : [ 0, 0.00000895 * 2, 0.00000895 * 3 ]
        , result : -1
        }
        , { suffix : "maxAcceleration"
        , input  : "altitude"
        , values : [ 0, 1, 3 ]
        , result : 1
        }
        ]
    , windSpeed:
        [ // No air speed, pur speed
          { suffix : "windSpeed"
          , input  : "longitude"
          , values : [ 0, 0.00000895 * 1, 0.00000895 * 2, 0.00000895 * 3, 0.00000895 * 4 ]
          , result : 1
          }
          , { suffix : "windSpeed"
          , input  : "air_speed"
          , values : [ 1, 1, 1, 1 ]
          , result : -1
          }
          , { suffix : "windSpeed"
          , input  : [ "air_speed", "longitude" ]
          , values :
          { "air_speed" : [ 1, 1, 1, 1, 1 ]
          , longitude   : [ 0, 0.00000895 * 1, 0.00000895 * 2, 0.00000895 * 3, 0.00000895 * 4 ]
          }
          , result: 0
          } ]
    , avgMachSpeed:
        { suffix : "avgMachSpeed"
        , input  : "longitude"
        , values : [ 0, 0.343 / ( 6371 / 360 * Math.PI * 2 ) ]
        , result : 1
        }
    , maxMachSpeed:
        { suffix : "maxMachSpeed"
        , input  : "longitude"
        , values : [ 0, 0, 0, 0.343 / ( 6371 / 360 * Math.PI * 2 ) ]
        , result : 1
        }
    , maxAccelG:
        { suffix : "maxAccelG"
        , input  : "longitude"
        , values : [ 0, 0.00008777 * 1, 0.00008777 * 3 ]
        , result : 1
        }

    }
  }
} ;
