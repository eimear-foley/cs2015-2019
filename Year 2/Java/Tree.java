/**
 * class 'Tree' - generic implementation of a recursive binary tree
 * @author Eimear Foley 115352866
 *
 * @param <T>
 */
public class Tree<T extends Comparable<T>> {
	private Tree<T> leftchild;
	private Tree<T> rightchild;
	private T elt;
	private int tab;
	
	/**
	 * Class Constructor
	 */
	public Tree(){
		this.elt = null;
		this.rightchild = null;
		this.leftchild = null;
		this.tab = 0;
	}
	
	/**
	 * Private class constructor for creating new subtrees 
	 * @param elt
	 * @param tab
	 */
	private Tree(final T elt, int tab){
		this.elt = elt;
		this.leftchild = null;
		this.rightchild = null;
		this.tab = tab;
	}
	
	/**
	 * Inserts new value 'elt' to tree
	 * @param elt
	 */
	public void insert(final T elt){
		if (this.elt == null){
			this.elt = elt;
		} else if (this.elt.compareTo(elt) > 0){
			if (this.leftchild == null){
				Tree<T> child = new Tree<T>(elt, tab + 1);
				this.leftchild = child;
			} else {
				this.leftchild.insert(elt);
			}
		} else if (this.elt.compareTo(elt) < 0){
			if (this.rightchild == null){
				Tree<T> child = new Tree<T>(elt, tab + 1);
				this.rightchild = child;
			} else {
				this.rightchild.insert(elt);
			}
		}
	}

	/**
	 * Helper function to 'showInOrder()', 'showPreOrder()', 'showPostOrder()'
	 * Creates space before elements in tree according to method of traversal
	 */
	public void tabify(){
		for (int i = 0; i < this.tab; i++){
			System.out.print(" ");
		}
	}

	/**
	 * Using pre-order traversal outputs binary tree in the following order:
	 * root, leftchild, rightchild
	 */
	public void showPreOrder(){
		if (elt != null){
			tabify();
			System.out.println(this.elt);
			if (this.leftchild != null){
				this.leftchild.showPreOrder();
			} 
			if (this.rightchild != null){
				this.rightchild.showPreOrder();
			}
		} 
	}

	/**
	 * Using post-order traversal outputs binary tree in the following order:
	 * leftchild, rightchild, root
	 */
	public void showPostOrder(){
		if (elt != null){
			if (this.leftchild != null){
				this.leftchild.showPostOrder();
			}
			if (this.rightchild != null){
				this.rightchild.showPostOrder();
			}
			tabify();
			System.out.println(this.elt);
		}
	}

	/**
	 * Using in-order traversal outputs binary tree in the following order:
	 * leftchild, root, rightchild
	 */
	public void showInOrder(){
		if (elt != null){
			if (this.leftchild != null){
				this.leftchild.showInOrder();
			}
			tabify();
			System.out.println(this.elt);
			if (this.rightchild != null){
				this.rightchild.showInOrder();
			}
		}
	}

	/**
	 * Test block
	 */
	public static void main(String[] args){
		final Tree<Integer> tree = new Tree<Integer>( );
		tree.insert( 1 );
		tree.insert( 2 );
		tree.insert( 0 );
		System.out.println("In-Order:");
		tree.showInOrder();
		System.out.println("Post-Order:");
		tree.showPostOrder();
		System.out.println("Pre-Order:");
		tree.showPreOrder();
	}
}
