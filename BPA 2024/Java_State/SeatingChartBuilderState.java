
import java.io.FileNotFoundException;
import java.io.File;
import java.util.*; 
import java.text.DecimalFormat;

public class SeatingChartBuilderState
   {

   public static void main (String args [])
      {
      
   
      inputManager(); 
     
      printStudents();
      printHighestGPA(); 
      printLowestGPA(); 
      
      }
  
   
    //Finds and prints the highest GPA from all the students
   private static void printHighestGPA() 
      {

      }
      
    //Finds and prints the lowest GPA from all the students       
   private static void printLowestGPA() 
      {
     
      }

    
   private static void setStudents(int nc)
      {
      Random rand = new Random();
      Students s;
      DecimalFormat df = new DecimalFormat("#.00");
      int nameCount = nc;
      double gpa;
      int grade;
      String fn; String ln;
      
      String [] allNames ={"Walter","Jones","Rose","Wilson" ,"Jack", "Rodriguez" , "Elizabeth" , "Smith", "Earl", "Carter", "Linda", "Ward", "Christopher", 
         "Turner", "Martin", "Murphy", "Betty", "Garcia", "Shawn", "Taylor","Sean", "Simmons", "Joshua", "Evans", "Norma", "Mitchell", "Brenda", "Johnson", "Donna", 
         "Clark", "Irene", "Diaz","Marilyn", "Coleman","Arthur", "Collins","Henry", "Hall","Howard", "Robinson","Jerry", "Green","Maria", "Price", "Evelyn", "Bell", 
         "Janet", "Moore", "Susan", "Foster"};
          
      for(int i =0; i<nameCount; i++)
         {
         
         do{
         
            fn = allNames[rand.nextInt(allNames.length)];
            ln = allNames[rand.nextInt(allNames.length)];
            }while(fn.equals(ln));
         grade = rand.nextInt(4)+9;
         double tempGPA = rand.nextDouble()*3.0 + 1.0;
         String  tempString =df.format(tempGPA);
         gpa = Double.parseDouble(tempString);
         s = new Students(fn,ln,grade,gpa);
         students.add(s);
         }
      
      }
   
   //Given   
   private static void printStudents(){
      int i = 1;
      for (Students n : students)
         {
         System.out.println(i+") "+n.getWholeName() + " | Grade Level: "+n.getGradeLevel()+" | GPA: "+n.getGPA());
         i++;
         }
   
      printHighestGPA(); 
      printLowestGPA();
      }
      
   //Gets user input commands and checks for entry errors     
   private static void inputManager()
      {
      
      }  


   }

class Students
   {
   //Create appropriately variables based upon constructor parameters
   //Generic Constructor  
   public Students()
      {
  
      }
    //Constructor with Parameters
   public Students(String fn, String ln, int gl, double gpa)
      {
  
      }
      
    //Returns "last name, first name" with appropriate variables
   public String getWholeName()
      {
      
      }
    //Returns first name
   public String getFirstName()
      {
      
      }
    //Returns last name  
   public String getLastName()
      {
      
      }
   //Returns the GPA   
   public double getGPA()
      {
      
      }
    //Returns grade level  
   public int getGradeLevel()
      {
      
      }
    

   }