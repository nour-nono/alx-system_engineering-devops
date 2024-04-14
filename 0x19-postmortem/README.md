postmortem
==========
This directory contains postmortem reports for incidents that have occurred in the past.

## Table of Contents

- [Incident Reports](#incident-reports)
- [Contributing](#contributing)

## Incident Reports

- [Incident #1: Outage on yyyy-mm-dd](./incident-1.md)

## Contributing

If you have experienced an incident and would like to contribute a postmortem report, please follow the steps below:

1. Create a new file in this directory with the name `incident-<number>.md`, where `<number>` is the next available number.
2. Use the [template](./template.md) to structure your report.
3. Fill in the details of the incident.
4. Submit a pull request with your changes.

    ```
    git add incident-<number>.md
    git commit -m "Add incident report for incident <number>"
    git push origin master
    ```

5. Your report will be reviewed and merged into the repository.
```
# example

# Path: 0x19-postmortem/incident-1.md
# Incident #1: Outage on yyyy-mm-dd


## Summary

On 2020-01-01, the system experienced an outage that lasted for 2 hours. The outage was caused by a hardware failure in the server hosting the application.

## Timeline

- 2020-01-01 10:00 AM: The system went down due to a hardware failure.
- 2020-01-01 10:30 AM: The operations team was alerted to the issue.
- 2020-01-01 11:00 AM: The team identified the cause of the outage as a hardware failure in the server.
- 2020-01-01 12:00 PM: The team replaced the faulty hardware and restored the system to normal operation.

## Impact

- The outage lasted for 2 hours.
- Users were unable to access the system during this time.
- The incident caused a loss of revenue for the company.

## Root Cause

The root cause of the outage was identified as a hardware failure in the server hosting the application. The failure was due to a faulty power supply unit.

## Resolution

To resolve the issue, the operations team replaced the faulty power supply unit with a new one. The system was then brought back online and normal operation was restored.

## Preventative Measures

To prevent similar incidents in the future, the following measures will be implemented:

- Regular hardware maintenance checks will be conducted to identify and replace faulty components.
- Redundant power supplies will be installed to provide backup in case of a failure.
- Monitoring systems will be put in place to alert the operations team of any hardware issues before they cause an outage.

## Lessons Learned

This incident highlighted the importance of regular hardware maintenance and monitoring. It also emphasized the need for redundancy in critical components to prevent single points of failure.

## Additional Information

- Incident Report: [incident-1.md](./incident-1.md)
- Postmortem Template: [template.md](./template.md)
