package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  A catalog element with a title and class classification
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IdentifiedElement extends CatalogElement {

  private String title;
  private String class;

}