const text: string = "Lorem Ipsum";
alert(text.toUpperCase());

const optionalText: string | null = true ? null : "";
if (optionalText !== null) alert(optionalText.toUpperCase());

const requiredText: string = optionalText ?? "(n/a)";
