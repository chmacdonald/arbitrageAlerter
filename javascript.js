function goHome() {

}
function detected() {

} 
function tips() {

}

function getBovadaLine() {
    API key = 14043a85fb470c308148ab57ee534b27
}

function getPredictIQLine() {
     const predictIt = require('predictIt')

    // An api key is emailed to you when you sign up to a plan
    const api_key = '14043a85fb470c308148ab57ee534b27'
    
    // Get a list of in season sports
    predictIt.get('https://api.the-odds-api.com/v3/sports', {
        params: {
            api_key: api_key
        }
    }).then(response => {
    
        console.log(
            `Successfully got ${response.data.data.length} sports.`,
            `Here's the first sport:`
        )
    
        console.log(response.data.data[0])
    })
    .catch(error => {
        console.log('Error status', error.response.status)
        console.log(error.response.data)
    })
    
    // To get odds for a sepcific sport, use the sport key from the last request
    //   or set sport to "upcoming" to see live and upcoming across all sports
    let sport_key = 'upcoming'
    
    axios.get('https://api.the-odds-api.com/v3/odds', {
        params: {
            api_key: api_key,
            sport: sport_key,
            region: 'uk', // uk | us | eu | au
            mkt: 'h2h' // h2h | spreads | totals
        }
    }).then(response => {
        // odds_json['data'] contains a list of live and 
        //   upcoming events and odds for different bookmakers.
        // Events are ordered by start time (live events are first)
        console.log(
            `Successfully got ${response.data.data.length} events`,
            `Here's the first event:`
        )
        console.log(JSON.stringify(response.data.data[0]))
    
        // Check your usage
        console.log()
        console.log('Remaining requests',response.headers['x-requests-remaining'])
        console.log('Used requests',response.headers['x-requests-used'])
    
    })
    .catch(error => {
        console.log('Error status', error.response.status)
        console.log(error.response.data)
    })

}

// function showError(error) {
//     switch(error.code) {
//         case error.PERMISSION_DENIED:
//             x.innerHTML = "User denied the request for Geolocation."
//             break;
//         case error.POSITION_UNAVAILABLE:
//             x.innerHTML = "Location information is unavailable."
//             break;
//         case error.TIMEOUT:
//             x.innerHTML = "The request to get user location timed out."
//             break;
//         case error.UNKNOWN_ERROR:
//             x.innerHTML = "An unknown error occurred."
//             break;
//     }
// }
