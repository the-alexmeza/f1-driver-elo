from .models import Circuit, Driver, Race
import pandas as pd
from multielo import MultiElo


def initializeDatabase(circuits="../data/circuits.csv", drivers="../data/drivers.csv", races="../data/races.csv", results="../data/results.csv"):
    print("Initializing database from CSVs...")
    print(f"Loading circuits from: {circuits}...")
    loadCircuitsFromDataFile(circuits)
    print("Circuits completed successfully!")
    print(f"Loading drivers from: {drivers}...")
    loadDriversFromDataFile(drivers)
    print("Drivers completed successfully!")
    print(f"Loading races from: {races}...")
    loadRacesFromDataFile(races)
    print("Races completed successfully!")
    print(f"Loading results from: {results}...")
    loadResultsFromDataFile(results)
    print("Results loaded successfully!")

    print("Processing results and updating Elo")
    setAllDriversElo()
    print("All drivers Elo successfully updated!")
    print("Initialization complete.")


def loadCircuitsFromDataFile(path):
    # TODO: no validation :o
    df_circuits = pd.read_csv(path)
    for _, row in df_circuits.iterrows():
        # handle nullable fields
        alt = None
        if type(row["alt"]) == int:
            alt = row["alt"]
        circuit = Circuit(id=row["circuitId"], circuitRef=row["circuitRef"], name=row["name"], location=row["location"],
                          country=row["country"], lat=row["lat"], lng=row["lng"], alt=alt, url=row["url"])
        circuit.save()


def loadDriversFromDataFile(path):
    # TODO: no validation :o
    df_drivers = pd.read_csv(path)
    for _, row in df_drivers.iterrows():
        # handle nullable fields
        number = None
        code = None
        if type(row["number"]) == int:
            number = row["number"]
        if row["code"] != "\\N":
            code = row["code"]
        driver = Driver(id=row["driverId"], driverRef=row["driverRef"], number=number, code=code, forename=row["forename"],
                        surname=row["surname"], dob=row["dob"], nationality=row["nationality"], url=row["url"])
        driver.save()


def loadRacesFromDataFile(path):
    # TODO: no validation :o
    df_races = pd.read_csv(path)
    for _, row in df_races.iterrows():
        circuit = Circuit.objects.get(id=row["circuitId"])
        race = Race(id=row['raceId'], year=row['year'], circuit=circuit,
                    name=row['name'], date=row['date'], url=row['url'])
        race.save()


def loadResultsFromDataFile(path):
    # TODO: validation
    df_results = pd.read_csv(path)
    races = Race.objects.all()
    for race in races:
        df = df_results.loc[df_results['raceId'] ==
                            race.id].sort_values(by='positionOrder')
        drivers = []
        for _, row in df.iterrows():
            driver = Driver.objects.get(id=row['driverId'])
            drivers.append((driver, int(row["positionOrder"])))

        drivers.sort(key=lambda x: x[1])  # probably don't need this
        race.addDriversAndResults(drivers)


def setAllDriversElo():
    elo = MultiElo()
    races = Race.objects.all()
    for race in races:
        try:
            result = [driver.elo for driver in race.drivers.all()]
            new = elo.get_new_ratings(result)
            for i, d in enumerate(race.drivers.all()):
                d.ChangeRating(race, new[i])
        except Exception as e:
            print(f"Failed Race Id: {race.id}. Error: {e}")
