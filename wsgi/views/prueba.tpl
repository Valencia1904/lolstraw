				<form id="formulario" method="post" action="/campeon/kingcong">
					<div>
						<h3>Nivel</h3>
						<select id="nivel" name="nivel">
%for i in xrange(1,19):
								<option value="{{i}}">{{i}}</option>
%end

						</select>
						<input type="submit" name="Enviar" value="calcular" />
					</div>
				</form>
