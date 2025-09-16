import * as yup from 'yup'

const getValidationSchema = (isStepTwo) =>
  yup.object().shape({
    phone: yup.string()
      .matches(/^09\d{9}$/, "شماره موبایل معتبر نیست")
      .required("شماره موبایل الزامی است")
      .when([], {
        is: () => isStepTwo, // توی مرحله دوم phone رو ولیدیت نکن
        then: (schema) => schema.notRequired(),
      }),
    code: yup.string()
      .matches(/^\d{6}$/, "کد باید ۶ رقم باشد")
      .required("کد الزامی است")
      .when([], {
        is: () => !isStepTwo, // توی مرحله اول code رو ولیدیت نکن
        then: (schema) => schema.notRequired(),
      }),
  });

export default getValidationSchema;
