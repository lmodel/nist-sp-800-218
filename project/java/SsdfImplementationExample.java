package example;

/* metamodel_version: 1.12.0 */
/* version: 1.1.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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