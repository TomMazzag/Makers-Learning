class Weather {
  constructor(client) {
    this.client = client;
  }

  async load(city) {
    this.data = await this.client.fetchWeatherData(city);
    return this.data;
  }

  getWeatherData() {
    return {
      City: this.data.name,
      Weather: this.data.weather[0].main,
      Temperature: Math.round(this.data.main.temp),
      Feels_like: Math.round(this.data.main.temp),
      Humidity: `${this.data.main.humidity}%`,
    };
  }
}

module.exports = Weather;
