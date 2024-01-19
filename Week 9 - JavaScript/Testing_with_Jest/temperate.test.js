class Thermostat {
    constructor() {
        this.temperature = 20;
        this.powerSaving = false;
    }

    getTemperature() {
        return this.temperature;
    }

    up() {
        if (this.powerSaving === false) {
            this.temperature++;
        } else if (this.temperature < 25) {
            this.temperature++;
        }
    }

    down() {
        this.temperature--;
    }

    setPowerSavingMode(value) {
        this.powerSaving = value;
    }

    reset() {
        this.temperature = 20;
    }
}

describe("Unit tests for Thermostat class", () => {
    test("Test temperature increases", () => {
        const thermostat = new Thermostat();
        thermostat.up();
        expect(thermostat.getTemperature()).toBe(21);
    });

    test("Test temperature decreases", () => {
        const thermostat = new Thermostat();
        thermostat.down();
        expect(thermostat.getTemperature()).toBe(19);
    });

    test("Test power saving mode", () => {
        const thermostat = new Thermostat();
        thermostat.setPowerSavingMode(true);
        for (let i = 0; i < 10; i++) {
            thermostat.up();
        }

        expect(thermostat.getTemperature()).toBe(25);
    });

    test("Test temperature can go over 25", () => {
        const thermostat = new Thermostat();
        thermostat.setPowerSavingMode(false);
        for (let i = 0; i < 10; i++) {
            thermostat.up();
        }

        expect(thermostat.getTemperature()).toBe(30);
    });

    test("Test temperature resets", () => {
        const thermostat = new Thermostat();
        thermostat.up();
        thermostat.reset();
        expect(thermostat.getTemperature()).toBe(20);
    });
});
