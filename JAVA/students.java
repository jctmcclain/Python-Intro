public class Students {
// Declarations
    public String username;
	public String firstname;
	public String lastname;
	public String eml;
	public String proglang;
// Constructor 
// Uses usernname to instance a class
	public Students(String username){
	    this.username = username;
	}
    // Setters
    public void setUsername(String newUsername){
        username = newUsername;
    }
	public void setFirstname(String newFname){
		firstname = newFname;
	}
	public void setLastname(String newLname){
	    lastname = newLname;
	}
	public void setEmail(String newEml){
	    eml = newEml;
	}
	public void setProglang(String newProglang){
	    proglang = newProglang;
	}
	// Getters 
	public String getUsername(){
	    return username;
	}
    public String getFirstname() {
        // System.out.println("First name is "+ firstname);
        return firstname;
    }
    public String getLastname() {
        // System.out.println("Last name is "+lastname);
        return lastname;
    }
    public String getEmail() {
        // System.out.println("Email is "+eml);
        return eml;
    }
    public String getProglang() {
       //  System.out.println("Programming Language is " + proglang);
        return proglang;
    }
    // Program Execution
    public static void main(String []args) {
        // Create a new instance
        Students compstudent = new Students("mcclait"); 
        // Set the parameters
        compstudent.setFirstname("Tom");
        compstudent.setLastname("McClain");
        compstudent.setEmail("mcclait@juniata.edu");
        compstudent.setProglang("Python");
        
        Students compstudent2 = new Students("wright");
        compstudent2.setFirstname("John");
        compstudent2.setLastname("Wright");
        compstudent2.setEmail("wright@juniata.edu");
        compstudent2.setProglang("Java");
        
        System.out.println(compstudent.getUsername());
        System.out.println(compstudent.getFirstname());
        System.out.println(compstudent.getLastname());
        System.out.println(compstudent.getEmail());
        System.out.println(compstudent.getProglang());
        System.out.println("-----------------------");
        System.out.println("-----------------------");
        
        System.out.println(compstudent2.getUsername());
        System.out.println(compstudent2.getFirstname());
        System.out.println(compstudent2.getLastname());
        System.out.println(compstudent2.getEmail());
        System.out.println(compstudent2.getProglang());
        System.out.println("-----------------------");
        System.out.println("-----------------------");
    }
}