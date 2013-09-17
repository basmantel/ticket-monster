package org.jboss.jdf.example.ticketmonster.model;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.util.regex.Pattern;

import javax.validation.Constraint;
import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;
import javax.validation.Payload;

/**
 * Validates that the code at bay is a valid cancellation code
 * 
 * @author emmanuel
 */
@Target({ElementType.FIELD, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy={CancellationCode.StringValidator.class})
public @interface CancellationCode {
	String message() default "org.jboss.jdf.example.ticketmonster.model.CancellationCode.message";
	Class<?>[] groups() default {};
	Class<? extends Payload>[] payload() default {};
	
	static final class StringValidator implements ConstraintValidator<CancellationCode, String> {

		private static Pattern uuidIgnoreCase = Pattern.compile("(?i)[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}");
		private static Pattern uuid = Pattern.compile("[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}");

		@Override
		public void initialize(CancellationCode annotation) {
		}

		@Override
		public boolean isValid(String value, ConstraintValidatorContext context) {
			if (value == null) {
				return true;
			}
			if (uuid.matcher(value).matches()) {
				return true;
			}
			if (uuidIgnoreCase.matcher(value).matches()) {
				context.disableDefaultConstraintViolation();
				context
					.buildConstraintViolationWithTemplate("The cancellation code should be in upper case")
					.addConstraintViolation();
				return false;
			}
			return false;
		}
	}
}
