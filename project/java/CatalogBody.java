package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  Main SSDF catalog object
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CatalogBody  {

  private String uuid;
  private Metadata metadata;
  private List<ControlGroup> groups;
  private BackMatter back-matter;

}