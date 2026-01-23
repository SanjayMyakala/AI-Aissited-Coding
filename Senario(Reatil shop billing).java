// provide code for retal store billing process and that should take customer name , the number of items purchased and name of the items purchased and take inputs of item name and cost in same line and then generate the total bill amount.
// Add discount feature based on total bill amount.If the total bill exceeds Rs. 500, apply a 5% discount, If the total bill exceeds Rs. 1000, apply a 10% discount, and if it exceeds Rs. 5000, apply a 15% discount, and if total bill greater than 10000 apply 20% discount.
// List items available in the store with their prices before taking inputs from user for purchased items. and if customer purchases same item multiple times then it should consider quantity of that item and calculate total cost accordingly.Take items like food items(like dals,rice,vegetables and etc),stationery items,cleaning items(soaps,detergents, etc) etc with their prices. Take list of 20 items in the store with their prices.
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
public class Senario {
    static Map<String, Double> storeItems = new HashMap<>();

    public static void main(String[] args) {
        initializeStoreItems();
        displayStoreItems();
        processCustomerPurchase();
    }

    static void initializeStoreItems() {
        storeItems.put("Rice", 50.0);
        storeItems.put("Wheat", 40.0);
        storeItems.put("Dal", 80.0);
        storeItems.put("Vegetables", 30.0);
        storeItems.put("Soap", 20.0);
        storeItems.put("Detergent", 100.0);
        storeItems.put("Notebook", 15.0);
        storeItems.put("Pen", 5.0);
        storeItems.put("Pencil", 3.0);
        storeItems.put("Eraser", 2.0);
        storeItems.put("Sugar", 45.0);
        storeItems.put("Salt", 10.0);
        storeItems.put("Oil", 120.0);
        storeItems.put("Spices", 60.0);
        storeItems.put("Bread", 25.0);
        storeItems.put("Butter", 70.0);
        storeItems.put("Cheese", 150.0);
        storeItems.put("Milk", 40.0);
        storeItems.put("Eggs", 90.0);
        storeItems.put("Chicken", 200.0);
    }

    static void displayStoreItems() {
        System.out.println("Available items in the store:");
        for (Map.Entry<String, Double> item : storeItems.entrySet()) {
            System.out.printf("%s: Rs. %.2f\n", item.getKey(), item.getValue());
        }
    }

    static void processCustomerPurchase() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter customer name: ");
        String customerName = sc.nextLine();

        System.out.print("Enter the number of different items purchased: ");
        int itemCount = sc.nextInt();
        sc.nextLine(); // Consume newline

        double totalBill = 0;

        for (int i = 0; i < itemCount; i++) {
            System.out.print("Enter item name and quantity : ");
            String input = sc.nextLine();
            String[] parts = input.split(" ");
            String itemName = parts[0];
            int quantity = Integer.parseInt(parts[1]);
            double itemPrice = storeItems.get(itemName);
            totalBill += itemPrice * quantity;
        }

        double discount = calculateDiscount(totalBill);
        double finalBill = totalBill - discount;

        System.out.println("Customer Name: " + customerName);
        System.out.println("Total Bill Amount: Rs. " + totalBill);
        System.out.println("Discount Applied: Rs. " + discount);
        System.out.println("Final Bill Amount: Rs. " + finalBill);
    }

    static double calculateDiscount(double totalBill) {
        if (totalBill > 10000) {
            return totalBill * 0.20;
        } else if (totalBill > 5000) {
            return totalBill * 0.15;
        } else if (totalBill > 1000) {
            return totalBill * 0.10;
        } else if (totalBill > 500) {
            return totalBill * 0.05;
        }
        return 0;
    }
}