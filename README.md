# test-generator
Scripts to generate test files

### Consider 2 data sets (2 ACMI files)
- normal flights
- bad weather flights

### Output:
- header
- csv (timestamp,longitude,latitude,altitude,roll,pitch,yaw,u,v,heading,air_speed,engine_0,engine_1,temperature_in,humidity_in,pressure_in,heart_rate,oxygen_mask)

### Generated problems
- missing column
- missing header
- incomplete header
- missing colnames
- csv with only 1 line
- csv with only 2 lines
- csv with only 3 lines
- csv in reverse order
- ascii 'dot' replaced with middle dot (. / ⋅)
- corrupted binary (\n to \r)

