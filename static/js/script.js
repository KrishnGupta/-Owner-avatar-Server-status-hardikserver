// Data received from server - These variables will be populated with data from the server
var serverStatus1 = "{{ data }}"; // Server 1 status
var serverStatus2 = "{{ server_status }}"; // Server 2 status

// Uptime percentages received from server
var uptimePercentage1 = "{{ uptime_percentage }}"; // Server 1 uptime percentage
var uptimePercentage2 = "{{ uptime_percentage }}"; // Server 2 uptime percentage

// Response times received from server
var responseTime1 = "{{ load }} ms"; // Server 1 response time
var responseTime2 = "{{ aapanal_load }} ms"; // Server 2 response time

/**
 * Function to update server status and uptime chart
 * @param {string} status - Status of the server ('Running' or 'Stop')
 * @param {string} iconId - ID of the element representing the status icon
 * @param {string} textId - ID of the element representing the status text
 * @param {string} uptimePercentage - Uptime percentage of the server
 * @param {string} barId - ID of the element representing the uptime bar
 * @param {string} responseBarId - ID of the element representing the response bar
 * @param {string} responseTime - Response time of the server
 * @param {string} detailsId - ID of the element representing the service details
 */
function updateServerInfo(status, iconId, textId, uptimePercentage, barId, responseBarId, responseTime, detailsId) {
    var statusIcon = document.getElementById(iconId);
    var statusText = document.getElementById(textId);
    var barElement = document.getElementById(barId);
    var responseBarElement = document.getElementById(responseBarId);
    var serviceDetailsElement = document.getElementById(detailsId);

    // Update server status
    if (status === "Running") {
        statusIcon.classList.add('online');
        statusIcon.classList.remove('offline');
        statusText.textContent = "Running";
        responseBarElement.classList.remove('hidden');
        responseBarElement.textContent = responseTime;
        serviceDetailsElement.classList.remove('hidden');
    } else {
        statusIcon.classList.add('offline');
        statusIcon.classList.remove('online');
        statusText.textContent = "Stop";
        uptimePercentage = 0; // Set uptime percentage to 0 if server is not running
        responseBarElement.classList.add('hidden');
        serviceDetailsElement.classList.add('hidden');
    }

    // Update uptime chart bar
    barElement.style.width = uptimePercentage + '%';
    barElement.textContent = uptimePercentage + '%';
}

/**
 * Function to update overall status message and banner
 * @param {string} status1 - Status of server 1
 * @param {string} status2 - Status of server 2
 */
function updateStatusMessage(status1, status2) {
    var statusMessage = document.getElementById('status-message');
    var statusBanner = document.getElementById('status-banner');
    if (status1 === "Running" && status2 === "Running") {
        statusMessage.textContent = "All services are online";
        statusMessage.className = "status-message all-services-online";
        statusBanner.src = 'static/images/right.png'; // Example right icon URL
    } else if (status1 === "Running" || status2 === "Running") {
        statusMessage.textContent = "One service online, one offline.";
        statusMessage.className = "status-message one-service-online";
        statusBanner.src = 'static/images/exclamation.png'; // Example exclamation icon URL
    } else {
        statusMessage.textContent = "Server Offline";
        statusMessage.className = "status-message server-offline";
        statusBanner.src = 'static/images/cancel.png'; // Example cancel icon URL
    }
}

// Update first server panel
updateServerInfo(serverStatus1, 'status-icon-1', 'status-text-1', uptimePercentage1, 'uptime-bar-1', 'response-bar-1', responseTime1, 'service-details-1');

// Update second server panel
updateServerInfo(serverStatus2, 'status-icon-2', 'status-text-2', uptimePercentage2, 'uptime-bar-2', 'response-bar-2', responseTime2, 'service-details-2');

// Update overall status message and banner
updateStatusMessage(serverStatus1, serverStatus2);
