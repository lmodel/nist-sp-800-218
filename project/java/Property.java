package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  A name-value property with optional namespace
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Property  {

  private String name;
  private String value;
  private String ns;

}