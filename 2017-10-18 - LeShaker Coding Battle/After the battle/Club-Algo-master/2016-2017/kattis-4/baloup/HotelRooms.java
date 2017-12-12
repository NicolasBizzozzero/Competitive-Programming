import java.util.Arrays;
import java.util.Scanner;

public class HotelRooms {
	
	
	public static void main(String[] args) {
		try (Scanner s = new Scanner(System.in)) {
			int nbRooms = s.nextInt();
			int nbBooked = s.nextInt();
			boolean[] booked = new boolean[nbRooms];
			Arrays.fill(booked, false);
			for (int i=0; i<nbBooked; i++) {
				booked[s.nextInt()-1] = true;
			}
			
			
			for (int i=0; i<nbRooms; i++) {
				if (!booked[i]) {
					System.out.println(i+1);
					return;
				}
			}
			System.out.println("too late");
		}
	}

}
