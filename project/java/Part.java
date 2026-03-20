package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  Structured narrative part containing prose content
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Part extends IdentifiedElement {

  private String name;
  private String prose;

}