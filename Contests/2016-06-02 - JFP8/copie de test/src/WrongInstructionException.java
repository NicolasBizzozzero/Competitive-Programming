/**
 * Created by twodn-1 on 02/06/16.
 */
public class WrongInstructionException extends RuntimeException{
    public String message;
    public WrongInstructionException(String message) {
        this.message = message;
    }
}
