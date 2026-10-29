package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  A notional implementation example: one type of tool, process or other method that could help implement a task.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SsdfImplementationExample  {

  private String description;
  private String exampleId;

}