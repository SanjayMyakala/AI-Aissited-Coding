//Provide code for An electricity billing system reads previous and current units and type of customer.
import java.util.Scanner;
public class lab3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter previous meter reading: ");
        int previousReading = sc.nextInt();
        System.out.print("Enter current meter reading: ");
        int currentReading = sc.nextInt();
        System.out.print("Enter customer type (R for Residential, C for Commercial): ");
        char customerType = sc.next().charAt(0);
        
        double billAmount = calculateBill(previousReading, currentReading, customerType);
        if (billAmount != -1) {
            System.out.printf("The electricity bill amount is: %.2f\n", billAmount);
        } else {
            System.out.println("Invalid customer type entered.");
        }
        sc.close();
    }
    
    public static double calculateBill(int previous, int current, char type) {
        int unitsConsumed = current - previous;
        double ratePerUnit;
        
        switch (type) {
            case 'R':
            case 'r':
                ratePerUnit = 5.0; // Residential rate
                break;
            case 'C':
            case 'c':
                ratePerUnit = 8.0; // Commercial rate
                break;
            default:
                return -1; // Invalid customer type
        }
        
        return unitsConsumed * ratePerUnit;
    }
}