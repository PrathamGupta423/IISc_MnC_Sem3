// import com.thealgorithms.datastructures.trees.SplayTree;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;



public class SplayTreeQuery {
    public static void main(String[] args) {

        int iters = Integer.parseInt(args[0]);
        System.out.println(iters);
        String outputFilePath = "output.txt";

        for(int j=1; j <= iters; j++){

            System.out.println(j);

            String filePath = "Inputs/input" + String.valueOf(j) + ".txt";
            Long Time1  =0L;
            Long TTime1 =0L ;
            Long Time2  =0L;
            Long TTime2 =0L ;
            Long Time3  =0L;
            Long TTime3 =0L ;
            Long Time4  =0L;
            Long TTime4 =0L ;
            Long Time5  =0L;
            Long TTime5 =0L ;

            int n1 = 0;
            int m1 = 0;
            int x1 = 0;
            String c1 = "";
            String h1 = "";


            for(int k=1 ; k<= 5; k++){

                // Step 1: Create a SplayTree instance
                SplayTree tree = new SplayTree();

                try {
                    // Step 2: Read from the file
                    Scanner scanner = new Scanner(new File(filePath));
                    
                    // Read 'n' (number of elements to insert)
                    int n = scanner.nextInt();
                    n1 = n;
                    scanner.nextLine();
                    // Insert 'n' numbers into the SplayTree
                    for (int i = 0; i < n; i++) {
                        int number = scanner.nextInt();
                        tree.insert(number);
                    }

                    int x = scanner.nextInt();
                    x1 = x;
                    scanner.nextLine();

                    // Read 'm' (number of queries)
                    int m = scanner.nextInt();
                    m1 = m;
                    scanner.nextLine();
                    long total_time = 0;
                    // Perform 'm' search queries on the SplayTree
                    long Full_time_S = System.nanoTime();
                    for (int i = 0; i < m; i++) {
                        int query = scanner.nextInt();
                        // Check if the queried number exists in the SplayTree
                        if(query == x){
                            long startTime = System.nanoTime();
                            tree.search(query);
                            long endTime = System.nanoTime();
                            total_time += endTime - startTime;
                            // System.out.println("Time taken: "
                        }
                        else{
                            tree.search(query);
                        }
                    }
                    long Full_time_E = System.nanoTime();
                    long Total_time2 = Full_time_E - Full_time_S;
                    scanner.nextLine();

                    String c = scanner.nextLine();
                    c1 = c;
                    String h = scanner.nextLine();
                    h1 = h;
                    // System.out.println(c);

                    if(k==1){
                        Time1 = total_time;
                        TTime1 = Total_time2;
                    }
                    else if(k==2){
                        Time2 = total_time;
                        TTime2 = Total_time2;
                    }
                    else if(k==3){
                        Time3 = total_time;
                        TTime3 = Total_time2;
                    }
                    else if(k==4){
                        Time4 = total_time;
                        TTime4 = Total_time2;
                    }
                    else if(k==5){
                        Time5 = total_time;
                        TTime5 = Total_time2;
                    }


                    scanner.close();
                } catch (FileNotFoundException e) {
                    System.err.println("File not found: " + filePath);
                }
            }

            long Average = (Time1 + Time2 + Time3 + Time4 + Time5)/5;
            long ATotal_time2 = (TTime1 + TTime2 + TTime3 + TTime4 + TTime5)/5;
            long Variance = ((Time1 - Average)*(Time1 - Average) + (Time2 - Average)*(Time2 - Average) + (Time3 - Average)*(Time3 - Average) + (Time4 - Average)*(Time4 - Average) + (Time5 - Average)*(Time5 - Average))/4;
            long Var2 = ((TTime1 - ATotal_time2)*(TTime1 - ATotal_time2) + (TTime2 - ATotal_time2)*(TTime2 - ATotal_time2) + (TTime3 - ATotal_time2)*(TTime3 - ATotal_time2) + (TTime4 - ATotal_time2)*(TTime4 - ATotal_time2) + (TTime5 - ATotal_time2)*(TTime5 - ATotal_time2))/4;
            // Step 3: Write the output to a file
            System.out.println(Time1 + "," + Time2 + "," + Time3 + "," + Time4 + "," + Time5 + "," + Average + "," + Variance + "," + ATotal_time2 + "," + Var2 + "," + h1);
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilePath, true))) {
                writer.write(x1 + "," + n1 + "," + m1 + "," + c1 + "," + Average + "," + Variance + "," +ATotal_time2+ "," + Var2 + "," +h1 + "\n");
                // System.out.println(x+"," + n + "," + m + "," + c + "," + total_time);
                // System.out.println("Time taken: " + total_time + " nanoseconds");
                // writer.write(total_time + "\n");
                // writer.newLine();
                // System.out.println("Time appended successfully.");
                // System.out.println("Absolute file path: " + new java.io.File("output1.txt").getAbsolutePath());
            } catch (IOException e) {
                System.err.println("Error writing to file: " + outputFilePath);
            }
        }
    }
}
