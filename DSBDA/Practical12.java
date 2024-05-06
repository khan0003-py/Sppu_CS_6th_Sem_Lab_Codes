package com.practical12;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String filename = "E:\\Eclipse Java Workspace\\Practical12\\src\\com\\practical12\\weather.txt";
        double[] sums = new double[3];
        int count = 0;

        try {
            Scanner scanner = new Scanner(new File(filename));
            while (scanner.hasNextLine()) {
                String[] data = scanner.nextLine().split(",");
                for (int i = 0; i < 3; i++) {
                    sums[i] += Double.parseDouble(data[i]);
                }
                count++;
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + filename);
            return;
        }

        double[] averages = new double[3];
        for (int i = 0; i < 3; i++) {
            averages[i] = sums[i] / count;
        }

        System.out.println("Average Temperature: " + averages[0]);
        System.out.println("Average Dew Point: " + averages[1]);
        System.out.println("Average Wind Speed: " + averages[2]);
    }
}
