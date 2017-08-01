/**
 * Class 'Cat' that implements behaviour of a cat
 * 
 * @author: Eimear Foley 115352866
 */
public class Cat {
    private static int cat_hunger = 3;
    private final Eat concreteEat;
    private final Roam concreteRoam;
    private final Noise concreteNoise;
     
    /**Class constructor
     * @param concreteEat
     * @param concreteRoam
     * @param concreteNoise
     */
    public Cat(){
        concreteEat = new ConcreteEat("I eat " + cat_hunger + " portions of food.");
        concreteRoam = new ConcreteRoam("I roam alone.");
        concreteNoise = new ConcreteNoise("Meow Meow");
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
        Cat Kitty = new Cat();
        Kitty.eat();
        Kitty.makeNoise();
        Kitty.roam();
    }
 
}
