/**
 * Created by twodn-2 on 02/06/16.
 */
public class QuadrupletEntier {
    private int nord_est;
    private int nord_ouest;
    private int sud_ouest;
    private int sud_est;

    public QuadrupletEntier(int ne, int no, int so, int se){
        nord_est = ne;
        nord_ouest = no;
        sud_ouest = so;
        sud_est = se;
    }

    public int getSud_est() {
        return sud_est;
    }

    public int getSud_ouest() {
        return sud_ouest;
    }

    public int getNord_ouest() {
        return nord_ouest;
    }

    public int getNord_est() {
        return nord_est;
    }
}
