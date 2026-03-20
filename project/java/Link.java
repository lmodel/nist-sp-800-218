package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  Relationship link with optional annotation text
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Link  {

  private String href;
  private String rel;
  private String text;

}