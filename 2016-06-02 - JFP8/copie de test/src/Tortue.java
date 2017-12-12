/**
 * Created by twodn-2 on 02/06/16.
 */
public class Tortue {
    private Orientation orientation;
    private int x, y;
    private Terrain terrain;

    public Tortue(Terrain terrain){
        orientation = Orientation.EST;
        x = 0;
        y = 0;
        this.terrain = terrain;
    }

    public void setPos(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void setOrientation(Orientation o)
    {
        this.orientation = o;
    }

    public void move(){
        switch (orientation){
            case EST:
                y += 1;
                break;
            case SUD:
                x -= 1;
                break;
            case OUEST:
                y -= 1;
                break;
            case NORD:
                x += 1;
                break;
        }
    }

    public void right(){
        switch (orientation){
            case EST:
                orientation = Orientation.SUD;
                break;
            case SUD:
                orientation = Orientation.OUEST;
                break;
            case OUEST:
                orientation = Orientation.NORD;
                break;
            case NORD:
                orientation = Orientation.EST;
                break;
        }
    }

    public void left(){
        switch (orientation){
            case EST:
                orientation = Orientation.NORD;
                break;
            case SUD:
                orientation = Orientation.EST;
                break;
            case OUEST:
                orientation = Orientation.SUD;
                break;
            case NORD:
                orientation = Orientation.OUEST;
                break;
        }
    }

    public void clear(){
        boolean valeur = terrain.getGrille()[y][x];

        if (valeur == true){
            terrain.getGrille()[y][x] = false;
            terrain.decrementeCompteur();
        }
    }

    public void plot(){
        boolean valeur = terrain.getGrille()[y][x];

        if (valeur == false){
            terrain.getGrille()[y][x] = true;
            terrain.incrementeCompteur();
        }
    }

    public Orientation getOrientation() {
        return orientation;
    }

    public int getY() {
        return y;
    }

    public int getX() {
        return x;
    }

    public boolean estSurCaseAllumée() {
        return terrain.getStatus(x,y);
    }

    public Terrain getTerrain() {
        return terrain;
    }
}
