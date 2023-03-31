# Personal Project - ClockifyAPI
This project uses Clockify API to retrieve information using the `x-api-key` header

## Commands
 `list`
 This command will show the las 30 entry times from the timesheet

 `create --description "value" --date "yyyy-MM-dd"`
 This command will create a new entry time with a default duration (8 hours) at the specified DATE

 ### Notes
An error will be raised if the date is not in the correct format

# TODO
- [ ] Give option to SSO (There's no provider, so ask for the APIKEY and set it as an env variable)
- [ ] Add option to select and delete a time record
- [ ] Add option to filter by date ranges
- [ ] Change date input from `str` to `date`

MIT License