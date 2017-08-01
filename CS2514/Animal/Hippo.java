/**
 * Class 'Hippo' that implements behaviour of a hippo.
 * 
 * @author: Eimear Foley 115352866
 */

public class Hippo implements Eat, Noise, Roam {
	private static int hippo_hunger = 10;
	private final Eat concreteEat;
	private final Roam concreteRoam;
	private final Noise concreteNoise;
	
	/**Class constructor
	 * @param concreteEat
	 * @param concreteRoam
	 * @param concreteNoise
	 */
	public Hippo(){
		concreteEat = new ConcreteEat("I eat " + hippo_hunger + " portions of food.");
		concreteRoam = new ConcreteRoam("I'm lazy, I don't roam.");
		concreteNoise = new ConcreteNoise("Grunt");
	}
	
	/**
	 * Implements 'roam()' method
	 * Prints animals roaming behaviour
	 */
	public void roam() {
		concreteRoam.roam();
	}
	
	/**
	 * Implements 'makeNoise()' method
	 * Prints animals noise behaviour
	 */
	public void makeNoise() {
		concreteNoise.makeNoise();
	}
	
	/**
	 * Implements 'eat()' method
	 * Prints animals eating behaviour
	 */
	public void eat() {
		concreteEat.eat();
	}
	
	/**
	 * Test block
	 */
	public static void main(String[] args){
		Hippo Herbert = new Hippo();
		Herbert.eat();
		Herbert.roam();
		Herbert.makeNoise();
	}

}
