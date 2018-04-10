while true; do
   curl -i -XPOST 'http://localhost:8086/write?db=pointdb' --data-binary @/root/pythonscripts/arduinoreadings
   sleep 10
done
