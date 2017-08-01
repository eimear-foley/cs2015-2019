/**
 * Class 'ConcreteNoise' that implements Interface 'Noise' 
 * to implement behaviour of an animal.
 * 
 * @author: Eimear Foley 115352866
 */
public class ConcreteNoise implements Noise {
	protected String noise;
	
	/**Class constructor
	 * @param noise
	 */
	public ConcreteNoise(final String noise){
		this.noise = noise;
	}
	
	/**
	 * Implements 'makeNoise()' method
	 * Prints animals noise behaviour
	 */
	@Override
	public void makeNoise(){
		System.out.println(noise);
	}
}
