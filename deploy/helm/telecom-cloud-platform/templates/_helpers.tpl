{{/*
Expand the name of the chart.
*/}}
{{- define "telecom-cloud-platform.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "telecom-cloud-platform.fullname" -}}
{{- include "telecom-cloud-platform.name" . }}
{{- end }}
