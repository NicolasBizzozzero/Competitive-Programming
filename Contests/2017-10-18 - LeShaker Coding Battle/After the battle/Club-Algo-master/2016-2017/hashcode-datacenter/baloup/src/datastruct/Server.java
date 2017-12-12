package datastruct;
public class Server {
	int row = -1, col = -1;
	public int group = -1;
	public final int size, capacity, index;
	
	Server(int s, int c, int i) {
		size = s;
		capacity = c;
		index = i;
	}
	
	Server(Server in) {
		this(in.size, in.capacity, in.index);
		row = in.row;
		col = in.col;
		group = in.group;
	}
	
	
	public boolean isValid() {
		return isPlaced() && isInGroup();
	}
	
	public boolean isPlaced() {
		return row >= 0 && col >= 0;
	}
	
	public boolean isInGroup() {
		return group >= 0;
	}
	
	
	@Override
	public String toString() {
		return isValid() ? (row + " " + col + " " + group) : "x";
	}
	

	
	public static int compareBySize(Server s1, Server s2) {
		return Integer.compare(s1.size, s2.size);
	}
	
	public static int compareByProfitability(Server s1, Server s2) {
		return Float.compare(s1.capacity/(float)s1.size, s2.capacity/(float)s2.size);
	}
	
	public static int compareBySizeThenByProfitabilityDesc(Server s1, Server s2) {
		int compSize = compareBySize(s1, s2);
		if (compSize != 0) return compSize;
		return -compareByProfitability(s1, s2);
	}
	
	

	
	@Override
	public boolean equals(Object obj) {
		if (obj == null || !(obj instanceof Server))
			return false;
		Server o = (Server) obj;
		return size == o.size
				&& capacity == o.capacity
				&& row == o.row
				&& col == o.col
				&& group == o.group;
	}
	
	public boolean equivalent(Server sv) {
		if (sv == null)
			return false;
		return size == sv.size
				&& capacity == sv.capacity;
	}
	
	@Override
	public int hashCode() {
		return size + capacity + row + col + group;
	}
	
	
}
