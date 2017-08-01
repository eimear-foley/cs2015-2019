/**
 * Class 'ConcreteEat' that implements Interface 'Eat' 
 * to implement behaviour of an animal.
 * 
 * @author: Eimear Foley 115352866
 */
public class ConcreteEat implements Eat{
	protected String eats;
	
	/**Class constructor
	 * @param eats
	 */
	public ConcreteEat(final String eats){
		this.eats = eats;
	}
	
	/**
	 * Implements 'eat()' method
	 * Prints animals eating behaviour
	 */
	@Override
	public void eat(){
		System.out.println(eats);
	}
}
