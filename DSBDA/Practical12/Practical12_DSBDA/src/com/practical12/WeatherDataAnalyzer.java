package com.practical12;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class WeatherDataAnalyzer {

    public static void main(String[] args) {
        // Path to the weather data file
        String filePath = "E:\\Eclipse Java Workspace\\Practical12_DSBDA\\src\\com\\practical12\\sample_weather.txt";
        
        // Read weather data from file
        double[][] weatherData = readWeatherData(filePath);
        
        // Calculate averages
        if (weatherData != null) {
            double[] averages = calculateAverages(weatherData);
            
            // Print the results
            System.out.println("Average Temperature: " + averages[0] + " °C");
            System.out.println("Average Dew Point: " + averages[1] + " °C");
            System.out.println("Average Wind Speed: " + averages[2] + " m/s");
        } else {
            System.out.println("No data found in the file.");
        }
    }

    // Function to read the weather data from the text file
    private static double[][] readWeatherData(String filePath) {
        try {
            File file = new File(filePath);
            Scanner scanner = new Scanner(file);

            List<double[]> validData = new ArrayList<>();

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] fields = line.split("\\s+");

                // Check if the line contains the expected number of fields
                if (fields.length >= 3) {
                    try {
                        double[] dataEntry = {
                                Double.parseDouble(fields[3]), // Temperature
                                Double.parseDouble(fields[4]), // Dew Point
                                Double.parseDouble(fields[5])  // Wind Speed
                        };
                        validData.add(dataEntry);
                    } catch (NumberFormatException e) {
                        // Skip lines with invalid data
                        continue;
                    }
                }
            }

            scanner.close();

            // Convert list to array
            double[][] weatherData = new double[validData.size()][3];
            for (int i = 0; i < validData.size(); i++) {
                weatherData[i] = validData.get(i);
            }

            return weatherData;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return null;
        }
    }

    // Function to calculate the average of each weather parameter
    private static double[] calculateAverages(double[][] weatherData) {
        int numEntries = weatherData.length;
        double[] averages = new double[3];
        
        double totalTemperature = 0;
        double totalDewPoint = 0;
        double totalWindSpeed = 0;
        for (double[] entry : weatherData) {
            totalTemperature += entry[0];
            totalDewPoint += entry[1];
            totalWindSpeed += entry[2];
        }
        
        averages[0] = totalTemperature / numEntries;
        averages[1] = totalDewPoint / numEntries;
        averages[2] = totalWindSpeed / numEntries;
        
        return averages;
    }
}