package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  Root wrapper for SSDF catalog content
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SSFDDocument  {

  private CatalogBody catalog;

}