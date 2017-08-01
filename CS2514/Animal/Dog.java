/**
 * Class 'Dog' that implements behaviour of a dog
 * 
 * @author: Eimear Foley 115352866
 */
public class Dog {
	private static int dog_hunger = 5;
	private final Eat concreteEat;
	private final Roam concreteRoam;
	private final Noise concreteNoise;
	
	/**Class constructor
	 * @param concreteEat
	 * @param concreteRoam
	 * @param concreteNoise
	 */
	public Dog(){
		concreteEat = new ConcreteEat("I eat " + dog_hunger + " portions of food.");
		concreteRoam = new ConcreteRoam("I roam in a pack.");
		concreteNoise = new ConcreteNoise("Bork Bork");
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
	public static void main(String[] args) {
		Dog Doggo = new Dog();
		Doggo.eat();
		Doggo.makeNoise();
		Doggo.roam();
	}

}
