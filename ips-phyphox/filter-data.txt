To filter messages in Phyphox when sending or receiving data, you can configure the experiment file to process only specific data or limit the scope of transmitted data. Here's how you can achieve this:
1. Use Buffers to Filter Data
Define specific buffers in your experiment to store only the required sensor data.
Example:
xml
<buffer id="filteredData" type="array"/>
2. Apply Filtering in the Analysis Block
Use modules like reduce or math in the analysis block to process raw sensor data before storing it in the buffer for transmission.
Example:
xml
<reduce input="rawData" output="filteredData" operation="average" count="10"/>
3. Control Data Transmission
Use the <send> tag with the keep attribute set to false to clear buffers after sending, avoiding duplicate data.
Example:
xml
<send id="filteredOutput" type="buffer" keep="false">filteredData</send>
4. Filter Unwanted Messages on the Server
If unwanted messages are still sent (e.g., due to timing), handle them server-side by discarding unnecessary data based on timestamps or content.
5. Trigger Data Transmission at Specific Times
Use a <timer> module or carefully set the interval property in the <connection> block to control when data is sent.
Example:
xml
<connection interval="5" address="http://yourserver.com/api" service="http/post" conversion="json">
    <send id="filteredOutput" type="buffer">filteredData</send>
</connection>