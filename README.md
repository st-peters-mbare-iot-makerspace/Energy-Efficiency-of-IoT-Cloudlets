# Process Level Evaluation of Energy Efficiency of Virtualised Databases in IoT cloudlets

The study intends to establish whether it is energy efficient to deploy database systems on a constrained gateway on a single board computer.  

## DHT22 Sensors
DHT22 sensors will be used in collecting temperature and humidity values from the atmosphere. 

## Arduino Uno R3 Microcontroller
An Arduino Uno microcontroller will be connected to a temperature/humidity sensors, running an Arduino program that formats the collected values.  

## Raspberry Pi 3 Single Board Computer
 The Arduino board will be connected to a Raspberry Pi 3 computer using the serial connection. The single board computers will store the read temperature and humidity values into a database. 

The experiments will utilise three different types of databases. The DHT22 sensors will be in close proximity to ensure the temperature and humidity readings and the environment are the same. At any given time, the time series applications will be similar. The similar measurements will be maintained for a week before a new application is used with all the variables i.e. sensors, databases remaining the same. The time-series applications will be developed in Python.

## Lightweight Operating Systems
Lightweight operating systems that will not significantly affect energy consumption will be installed on the Raspberry Pi. A trimmed down version of the official Raspbian operating system will deployed in some of the testbeds. Since the effect of Docker containers is central to this study a Docker optimised operating that is lightweight, Hypriot, will be used in some of the experiments as well.

## Systemd Services and Timers
Each python application that was used to query the databases would have five systemd services associated with it. The first service is a timer service that is configured with the time when the service should start. The second service is responsible for starting two other services namely the meter service which spawns the PowerAPI power meter. Its also starts the save service which takes the metrics developed by the power meter saving them into an SQLite database for future analysis. The fourth service is a timer that is configured with the time the service should be stopped. The last service is the service that actually stops the service. 

## HTTP APIs 
An HTTP API exposes a database to be queried transparently using any standard HTTP client such as curl. The study will test the energy efficiency of databases when processing queries through HTTP APIs. InfluxDB has built-in HTTP API support, thus additional API component when querying InfluxDB is not required. Prest will be used as the HTTP API interface of Postgres whilst Restheart will be used for MongoDB

## Generalisable Power Meters
Power meters will be developed from identifying the individual application and database processes and threads using systemd services. Scala objects also known as actors will be used to measure the power consumption. The Sensor actor will collect raw measurements from the underlying system forwarding them to the Formula Actor. The Formula Actor will in turn compute power estimation by implementing the power model. The Aggregator actor then aggregates power estimations using dimensions like process identifier or timestamp. Finally, the Reporter then formats estimations into a more readable way. 

## Energy Measurement and Saving Pipelines (PowerAPI)
The PowerAPI middleware software has to be configured to generate a software energy model that learns the CPU and using regression generates the power measurements. A general measurement pipeline that PowerAPI uses is shown in Figure 2.

Several power meters are spawn for every process in the system; they include:

1. The entire system (meter-system)
2. Python application that reads data from the Arduino microcontroller (meter-pypull-inserts, meter-pypush-inserts)
1. Python application that receives data from the database (meter-pypull-selects, meter-pypush-selects)
2. HTTP API that connects the python application to the database (meter-restheart, meter-prest)
3. The Database server (meter-influxdb, meter-mongodb, meter-postgres)

Scheduling the spawning of the processes is controlled by systemd timers. Figure 3 illustrates the steps that the scheduler follows as pipeline steps followed in a typical experiment:


The steps are is summarised as follows:
1. The App-system-docker.timer is configured to start executing at a specific time. 
2. When the specific time elapses the App-System service starts, and 
3. Spawns a Docker container which and at the same time 
4. Start a bash script that creates a PowerAPI power that starts computing the power consumption of the entire system and subsequently starts another bash that 
5. Reads the energy metrics extracting the energy value and timestamp adds the 	name of the system event and saves the values in an SQLite table within a 	database.


BASIC STEPS FOR ALL MACHINES
1. Software Setup(general/software-setup)
2. Network Setup(networking/network-setup)
3. Copy powerapi to Raspberry Pi root directory(powerapi/powerapi-cli) SOURCE:https://github.com/Spirals-Team/powerapi/releases
