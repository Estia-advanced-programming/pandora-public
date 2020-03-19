export const toDo = { milestones:
  { milestone1:
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
  }
} ;
