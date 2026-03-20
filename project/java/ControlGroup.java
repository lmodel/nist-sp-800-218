package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  An SSDF practice group (e.g. PO, PS, PW, RV)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlGroup extends IdentifiedElement {

  private List<Control> controls;

}