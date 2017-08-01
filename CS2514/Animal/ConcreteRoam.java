/**
 * Class 'ConcreteRoam' that implements Interface 'Roam' 
 * to implement behaviour of an animal.
 * 
 * @author: Eimear Foley 115352866
 */
public class ConcreteRoam implements Roam {
	protected String roam;
	
	/**Class constructor
	 * @param roam
	 */
	public ConcreteRoam(final String roam){
		this.roam = roam;
	}
	
	/**
	 * Implements 'roam()' method
	 * Prints animals roaming behaviour
	 */
	@Override
	public void roam(){
		System.out.println(roam);
	}

}
