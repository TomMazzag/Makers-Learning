const keys = require("./keys");

class WeatherClient {
  constructor() {
    this.apiKey = keys.weather;
  }

  async fetchWeatherData(city) {
    const apiUrl = `http://api.openweathermap.org/data/2.5/weather?units=metric&q=${city}&appid=${this.apiKey}`;
    const response = await fetch(apiUrl);
    const weatherData = await response.json();
    return weatherData;
  }
}

module.exports = WeatherClient;

/* const client = new WeatherClient();

client.fetchWeatherData("London").then((weatherData) => {
  console.log(`Weather data for ${weatherData.name}:`);
  console.log(weatherData);
}); */
