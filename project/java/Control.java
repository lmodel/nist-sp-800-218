package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  An SSDF practice containing tasks
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Control extends IdentifiedElement {

  private List<Task> controls;

}